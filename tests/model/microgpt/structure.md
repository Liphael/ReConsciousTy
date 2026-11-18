# microgpt(from bottom up)
下面把 `microgpt.py` 的流程改写成范畴视角：  
- **对象 Ob(C)**：数据、状态、类型、中间结果。  
- **态射 Hom(C)**：方法、函数、运算符、调用、转换。  
- **态射连接对象**：用 `对象 --态射--> 对象` 表示。  
- 多输入态射用积对象 `(A, B)` 表示；自环表示同类型二元运算。

---
## 1. 对象与态射约定

### 对象 Ob(C)

| 对象 | 含义 |
|---|---|
| `RawFile` | `input.txt` 原始文件 |
| `Docs` | 文档列表 `list[str]` |
| `CharSet` / `Vocab` / `BOS` | 字符集、词表、特殊 token |
| `TokenIDs` / `TokenID` / `PosID` | token 序列、当前 token、位置 |
| `StateDict` / `Params` / `WeightMatrix` | 参数字典、扁平参数、权重矩阵 |
| `Scalar` | 普通数值 |
| `ValueNode` | 自动微分标量节点 |
| `VectorValue` | `Value` 向量 |
| `Logits` / `Probs` | 未归一化分数 / 概率 |
| `Loss` / `Gradients` / `TopoOrder` | 损失、梯度、拓扑序 |
| `KVCache` | 每层 keys/values 缓存 |
| `HiddenState` / `Q` / `K` / `V` | 前向中间状态 |
| `AttnLogits` / `AttnWeights` / `AttnOut` | 注意力中间量 |
| `MLPOut` | MLP 输出 |
| `Moments` / `UpdatedParams` | Adam 动量 / 更新后参数 |
| `Temperature` / `SampleToken` / `SampleString` | 推理采样相关 |
| `State` | 训练循环状态 |

### 态射 Hom(C)

| 态射 | 源 → 目标 |
|---|---|
| `load_docs` | `RawFile → Docs` |
| `tokenize` | `Docs → (CharSet, TokenIDs, Vocab, BOS)` |
| `matrix` | `(nout, nin, std) → WeightMatrix` |
| `Value.__init__` | `(Scalar, children, local_grads) → ValueNode` |
| `__add__` / `__mul__` / `__sub__` / `__truediv__` | `(ValueNode, ValueNode) → ValueNode` |
| `__pow__` | `(ValueNode, Scalar) → ValueNode` |
| `__radd__` / `__rsub__` / `__rmul__` / `__rtruediv__` | `(Scalar, ValueNode) → ValueNode` |
| `__neg__` / `log` / `exp` / `relu` | `ValueNode → ValueNode` |
| `build_topo` | `ValueNode → TopoOrder` |
| `backward` | `Loss → Gradients` |
| `linear` | `(VectorValue, WeightMatrix) → VectorValue` |
| `softmax` | `Logits → Probs` |
| `rmsnorm` | `VectorValue → VectorValue` |
| `gpt` | `(TokenID, PosID, KVCache, Params) → Logits` |
| `loss_t` | `(Probs, TokenID) → Loss` |
| `average_loss` | `List<Loss> → Loss` |
| `adam_update` | `(Params, Gradients, Moments, lr) → (UpdatedParams, Moments)` |
| `sample` | `(Probs, Temperature) → TokenID` |
| `train_step` | `(Docs, Params, State) → (UpdatedParams, Loss)` |
| `infer` | `(BOS, Params, Temperature) → SampleString` |

---

## 2. 范畴总图



## 3. 依照结构的目的性拆解说明
[注释附件](structure_notes.md)

1. 准备原始输入，即对象“原始文件”，对应变量名：`RawFile`，`input.txt`（类型：文本文件）。
2. 设计编码器，即对象“Tokenizer”，并对应有解码器，即对象“Detokenizer”，Tokenizer以“编码”为目的，执行如下操作：
    - （主要）生成对象“文本词汇表（uchar）”：docs => sorted(set(''.join(docs))) => uchar
    - （优化）生成对象“文本词汇表数量标记（BOS）”：uchar => len(uchars) => BOS
    - （优化）生成&展示对象“计算词汇表数量值（vocab_size）”：uchar => len(uchars) + 1 => vocab_size
3. 设计自动求导/梯度单元，即对象“Autograd(itude)”（源文件中对应“Value”python类），Autograd以“构建神经网络计算图，以链式法则计算反向传播梯度”为目的，执行如下操作：
"""注：该Value类是一个巧妙的统一化对象，将所有的计算过程输出均归于此类，如同一个规范化的积木零件。而要区分结构中的节点、权重、偏差等具体概念，则要辨明该Value在这个积木零件搭成的结构中所处的计算位置。"""
    - （主要）生成对象“初始化对象Value”（源文件中对应特殊方法“__init__”）；使得对于每个“Value”类，保存一个数值“data”，对应一个梯度“grad”，保存一组子节点（**输入节点**）“children”，保存一组对应各输入节点偏导数的局部梯度“local_grads”：data => Value.data, 0 => Value.grad, children => Value.children, local_grads => Value.local_grads
    - （主要）定义“Value”专用态射“加法（add）”（源文件中对应特殊方法“__add__”）；使得对于每一个“Value”类，可以使用“+”运算。该态射首先检测“+”运算的右对象“other”（右操作数）是否是“Value”类，若不是则将其转化为“Value”类以满足运算格式要求。随后记录两者的局部偏导数均为1（加法），生成并返回一个新的“Value”类作为新节点，记录“self”和“other”为其子节点。
    - （主要）定义“Value”专用态射“乘法（multiply）”（源文件中对应特殊方法“__mul__”）；使得每个“Value”类，可以使用“\*”运算。该态射首先检测“\*”运算的右对象“other”（右操作数）是否是“Value”类，若不是则将其转化为“Value”类以满足运算格式要求。随后记录两者的局部偏导数，生成并返回一个新的“Value”类作为新节点，记录“self”和“other”为其子节点。
    - （主要）定义“Value”专用态射“幂运算（power）”（源文件中对应特殊方法“__pow__”）；使得每个“Value”类，可以使用“\*\*”运算。该态射右对象是否是“Value”类，因其为一常数，不再涉及作为“Value”类值的更新和计算。随后记录该幂运算的局部梯度$\frac{d(x^n)}{dx}= n*x^(n-1)$，生成并返回一个新的“Value”类作为新节点，记录“self”为其子节点。
    - （主要）定义“Value”专用态射“幂运算（power）”（源文件中对应特殊方法“__pow__”）；使得每个“Value”类，可以使用“\*\*”运算。该态射右对象是否是“Value”类，因其为一常数，不再涉及作为“Value”类值的更新和计算。随后记录该幂运算的局部梯度$\frac{d(x^n)}{dx}= n*x^(n-1)$，生成并返回一个新的“Value”类作为新节点，记录“self”为其子节点。

    


