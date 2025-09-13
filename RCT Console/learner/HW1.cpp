#include <iostream>
/*
* 头文件iostream 是C++标准库中的一个头文件；
其目的是为了提供输入输出功能的支持。
*/

// using namespace std;  
/*
* 命名空间namespace 是一个将能指标识符（用于指定变量、函数、类等的名称）组织在一起的容器；
其目的是为了避免命名冲突。
在大型项目中，不同的库或模块可能会定义相同名称的变量或函数，使用命名空间可以将它们区分开来。
在开头的直接调用命名空间的写法，将覆盖整个文件中的所有标识符，这是较为危险的；
建议在函数中调用命名空间，或者明确使用的命名空间前缀。

int main() 是C++程序的主函数，是程序执行的入口点；
每个C++程序都必须包含一个main函数，程序从这里开始执行，并在执行完毕后返回一个整数值给操作系统。
return 0; 表示程序成功结束，并将整数值0返回给操作系统；

注意，main()函数不支持重载和递归调用。
什么是重载？函数重载是指在同一个作用域内，可以定义多个同名但参数列表不同的函数；
什么是递归？递归是指函数直接或间接调用自身，以解决问题的一种编程技术。
何时使用递归？递归通常用于解决可以被分解为更小的相似子问题的问题，例如计算阶乘、斐波那契数列等；而在其他情况下，迭代通常更高效且易于理解。
*/

/*
int main()
{
	using namespace std;
	cout << "HW 1" << endl;
	system("pause");
	return 0;
}


int main()
{
	std::cout << "HW 2" << std::endl;
	system("pause");
	return 0;
}


int main()
{
	using namespace std;
	int a = 10;
	cout << "a = " << a << endl;
	system("pause");
	return 0;
}


int main()
{
#define days_per_week 7 // 宏定义常量
	using namespace std;
	cout << "There are " << days_per_week << " days in a week." << endl;
	system("pause");
	return 0;
}

int main()
{
	const int days_per_week = 7; // const定义常量
	using namespace std;
	cout << "There are " << days_per_week << " days in a week." << endl;
	system("pause");
	return 0;
}
*/

