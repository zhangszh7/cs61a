#### Problem

#### Chapter 1.3 Defining New Functions
**the intrinsic name** 和 a bound name 不同，一个函数只有一个intrinsic name，但可以有多个bound name。

函数定义时，注意命名的重要性，包括函数名和形参名（formal parameters）
- 函数名小写，下划线分隔，描述型名称
- 函数的名字通常暗示了（解释器对参数）执行的操作（例如 print, add, square），或者是计算得出的结果数值的名称（例如 max, abs, sum）
- 参数名小写，下划线分隔，最好单个词
- 参数名应该暗示其代表参数的作用，而非仅仅代表参数类型
- 拿单个字母作为参数名（如果参数的作用很明显）也是可以接受的，但是避免使用 l、O、I 这些容易和数字混淆的的字母

函数是一种抽象，可以从**domain、intent、range**这三个维度来理解，对应数学里的，定义域、映射关系、值域。

注意：/ 返回的是浮点型（对应truediv），而 // 返回整型（对应floordiv）


