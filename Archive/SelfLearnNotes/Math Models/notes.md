# NOTES

## L1

- “模态抽象”可理解为：可能状态/可能世界集合/概率空间 $(\Omega)$。
- “某一具体模态”：可理解为其中一个事件或命题 $(A \subseteq \Omega)$。
- “给定信息/已知信息”：可理解为条件 $(I\subseteq \Omega)$，若随时间不断完善则实际为一组递增$\sigma$-函数，在事件A是最终信息可测的定义假设下（即：事件指示随机变量$1_{A}\in F_{\infty}$，注意，可测意味着“可知”而非“已知”），其最终信息为：
    $$
    [
        F_{\infty}=\sigma(\bigcup^{\infty}_{n=1}F_{n})
    ]
    $$
- “基于给定信息发生的概率”：就是条件概率  
  $$
  [
  P(A\mid I)=\frac{P(A\cap I)}{P(I)}.
  ]
  $$

更准确的说法是：

> 概率是在某个可测的可能状态空间上，对事件赋予测度，并依据给定信息进行条件化的结果。模态抽象提供“可能空间”，给定信息提供“条件约束”，具体模态是测度所指向的对象；但概率的真正来源或解释，取决于频率、倾向、主观置信或逻辑对称等额外机制。

- 最简洁的结论：**模态抽象给出可能性，信息给出条件，测度才给出概率。具体模态不是概率的来源，而是概率被赋予的对象。**

最终的推导结论为：Doob鞅收敛定理

衍生状态模型
    - “效果随机”模型：属于日常绝大多数的情况，由于无信息导致的看似随机状态。
    - “真随机”模型：量子力学-“波函数坍缩真随机假设”

## L2

信息 versus 噪声：实践可归类入情报学

灰天鹅 versus 黑天鹅：多级冗余设计 + 识别全新模态

## L3

运算法则的数值机制：
    加法模型
    乘法模型
    幂律模型

## L4

优先连接模型（优先级幂律模型）

## Dimension Emergence Theory

数学形式：判定涌现何时发生
- 信息闭包
- 因果闭包
- 计算封闭

## Integration

Integration: in Parameter Space, the accumulation of a parameter's value to a orthogonal parameter. Notice that it is in parameter space, in actual system the actual variable represented by parameters can be non-orthogonal, for example the work done by force is the integration of force to the distance.

from this view, the Addition can be seen as a particular example of integration in Measure Theory.

## Differential Equations

the essence of differential equations is: given a local or differential relationship, solving the function that depict complete system behavior by integration and conditions of fixed/given solution.

## Information Theory

### Semiotics: Information Representation & Compression


