# 蜕变关系

该文档主要记录识别的蜕变关系。为了下文方便描述做以下定义：

stc: 原始测试用例

ftc: 衍生测试用例   

JB: 普通Java对象

## 蜕变关系1 （适用所有测试用例，不能揭示故障）

ftc的json文件通过在stc的json文件中每一个键对应值的末尾添加一行注释得到；stc与ftc的JB完全一致；如果存在一个stc与ftc中名字一样的成员变量具有不同的值，该蜕变关系被违反。
```
SF文件内容：
{
	"1": {
		"airClass": 2,
		"area": 0,
		"economicfee": 5153.698093040778,
		"luggage": 22.281053775603675,
		"student": false
	},
	"2": {
		"airClass": 3,
		"area": 0,
		"economicfee": 1936.2340923480338,
		"luggage": 48.14329753468175,
		"student": false
	}
}

FF文件内容：
{
	"1": {
		"airClass": 2,/*这是注释*/
		"area": 0,/*这是注释*/
		"economicfee": 5153.698093040778,/*这是注释*/
		"luggage": 22.281053775603675,/*这是注释*/
		"student": false/*这是注释*/
	},/*这是注释*/
	"2": {
		"airClass": 3,/*这是注释*/
		"area": 0,/*这是注释*/
		"economicfee": 1936.2340923480338,/*这是注释*/
		"luggage": 48.14329753468175,/*这是注释*/
		"student": false/*这是注释*/
	}/*这是注释*/
}

```

## 蜕变关系2（适用所有的测试用例，不能揭示故障）

ftc的待反序列化对象是将stc的json文件转化为字节后得到的字节数组；stc与ftc的JB完全一致；如果存在一个stc与ftc同名的成员变量具有不同的值，该蜕变关系被违反。

## 蜕变关系3

ftc的反序列化的对象是将stc的json文件转化为字符串后的结果；stc与ftc的JB完全一致；如果存在一个stc与ftc同名的成员变量具有不同的值，该蜕变关系被违反。

```
SF文件内容：
{
	"1": {
		"airClass": 2,
		"area": 0,
		"economicfee": 5153.698093040778,
		"luggage": 22.281053775603675,
		"student": false
	}
}

FF文件内容
\"1\": {\"airClass\": \"2\", \"area\": \"0\", \"economicfee\": \"5153.698093040778\", \"luggage\": \"22.281053775603675\", \"student\": \"false\"}

```

## 蜕变关系4（适用部分测试用例，揭示故障1和2）

如果stc的json文件中包含float类型的变量，则ftc在该变量值的末尾随机添加7位有效数字得到ftc的json文件；stc与ftc的JB完全一致；如果stc与ftc中该变量值的前7位数字完全相同，则该MR没有被违反。

```
SF文件内容：
{
	"1": {
		"airClass": 2,
		"area": 0,
		"economicfee": 5153.6,/*假设为float类型*/
		"luggage": 22.2,/*假设为float类型*/
		"student": false
	}
}

FF文件内容

{
	"1": {
		"airClass": 2,
		"area": 0,
		"economicfee": 5153.61234567,/*假设为float类型*/
		"luggage": 22.21234567,/*假设为float类型*/
		"student": false
	}
}
```

## 蜕变关系5（适用部分测试用例）

如果stc的json文件中包含double类型的变量，则ftc在该变量值的末尾随机添加16位有效数字得到ftc的json文件；stc与ftc的JB完全一致；如果stc与ftc中该变量值的前16位数字完全相同，则该MR没有被违反。

```
SF文件内容：
{
	"1": {
		"airClass": 2,
		"area": 0,
		"economicfee": 5153.6,/*假设为double类型*/
		"luggage": 22.2,
		"student": false
	}
}

FF文件内容

{
	"1": {
		"airClass": 2,
		"area": 0,
		"economicfee": 5153.61234567891234567,/*假设为double类型*/
		"luggage": 22.21234567,
		"student": false
	}
}
```

## 蜕变关系6（适用部分测试用例，揭示故障3）

stc的JB中存在一个成员变量为枚举类型，stc的josn文件中该变量的值是任意一个枚举对象中的元素。ftc将枚举类型的成员变量的值替换为不是枚举对象候选的值得到ftc的json文件；stc与ftc的JB完全一致；如果ftc的JB对象中枚举类型的成员变量的值不为“null”，或其它成员变量的值与SO不相同，该蜕变关系被违反。


```
SJB文件：
enum Code {
  SUCCESS, FAILURE
}

public class Num {
  private int id;
  private Code code;
  //getter and setter
}

SF文件内容：
{
  "code":SUCCESS
  "id":1
}

FF文件内容：
{
  "code":ERROR
  "id":1
}

```

## 蜕变关系7（适用部分测试用例）

ftc将stc的josn文件中表示日期的值用其它格式的形式表示，其它内容不变；stc与ftc的JB完全一致；如果ftc的JB对象中除了日期成员变量，存在一个成员变量的值与stc的JB对象不同或者ftc与stc的JB对象中表示日期的成员变量值不是同一个时间点，则该蜕变关系被违反。


## 蜕变关系8 （适用所有的测试用例）

ftc的JB将stc的JB中的成员变量的名字用蛇形结构表示，并且ftc的josn文件和stc的json文件相对应的成员变量的值相同。如果ftc和stc的JB对象中对应成员变量的值不同，该蜕变关系被违反。

```
stc的JB文件内容：
public class Num {
  private string testSuite;
  //getter and setter
}
ftc的JB内容
public class Num {
  private string test_Suite;
  //getter and setter
}
stc的json文件
{
  "testSuite": "a"
}
ftc的json文件
{
  "test_Suite":“a”
}
```

## 蜕变关系9 （适用所有的测试用例)

ftc的JB将stc的JB中的成员变量的名字用大驼峰结构表示，并且ftc的josn文件和stc的json文件相对应的成员变量的值相同。如果ftc和stc的JB对象中对应成员变量的值不同，该蜕变关系被违反。

```
stc的JB文件内容：
public class Num {
  private string testSuite;
  //getter and setter
}
ftc的JB内容
public class Num {
  private string TestSuite;
  //getter and setter
}
stc的json文件
{
  "testSuite": "a"
}
ftc的json文件
{
  "TestSuite":“a”
}
```

## 蜕变关系10 （适用所有的测试用例)

ftc的JB将stc的JB中的成员变量的名字用大驼峰结构表示，并且ftc的josn文件和stc的json文件相对应的成员变量的值相同。如果ftc和stc的JB对象中对应成员变量的值不同，该蜕变关系被违反。

## 蜕变关系11 （适用部分测试用例，List置换）

​	ftc的json文件将stc的json文件中列表中的元素进行置换，stc与ftc的JB完全一样，如果ftc的JB对象的List实例与stc的JB对象的List实例中顺序不相反或者stc的JB对象的List中的内容没有完全出现在ftc的JB对象的List实例中，该蜕变关系被违反。

## 蜕变关系12（适用部分测试用例，List插入）

​	ftc的json文件在stc的json文件中列表中插入一个新的元素，stc与ftc的JB完全一样，如果ftc的JB对象的List实例不包含stc的JB对象的List实例中的所有元素以及新插入的元素，该蜕变关系被违反。

## 蜕变关系13 （适用部分测试用例，List删除）

​	ftc的json文件将stc的json文件中列表中的最后一个元素删除，stc与ftc的JB完全一样，如果ftc的JB对象的List实例添加删除的元素之后与stc的JB对象的List实例不相等，该蜕变关系被违反。

## 蜕变关系14（适用部分测试用例，List拆分）

ftc的json文件将stc的json文件中列表的元素均分到两个列表中，ftc的JB对象创建两个List对象存放元素，如果ftc的JB对象中的两个List实例的元素之和与stc的JB对象的List实例中的元素不相等，该蜕变关系被违反。

## 蜕变关系15（适用部分测试用例，Map插入）

​	ftc的json文件在stc的json文件中的Map中插入一个新的键值对，stc与ftc的JB完全一样，如果ftc的JB对象的Map实例不包含stc的JB对象的Map实例中的所有元素以及新插入的键值对，该蜕变关系被违反。

## 蜕变关系16 （适用部分测试用例，Map删除）

​	ftc的json文件将stc的json文件中列表中的最后一个键值对，stc与ftc的JB完全一样，如果ftc的JB对象的Map实例添加删除的键值对之后与stc的JB对象的Map实例不相等，该蜕变关系被违反。

## 蜕变关系17（适用部分测试用例，Map拆分）

ftc的json文件将stc的json文件中Map的键值对均分到两个Map中，ftc的JB对象创建两个Map对象存放键值对，如果ftc的JB对象中的两个Map实例的键值对之和与stc的JB对象的Map实例中的键值对不相等，该蜕变关系被违反。

## 蜕变关系18（适用部分测试用例，Set插入）

​	ftc的json文件在stc的json文件中集合中插入一个新的元素，stc与ftc的JB完全一样，如果ftc的JB对象的List实例不包含stc的JB对象的List实例中的所有元素以及新插入的元素，该蜕变关系被违反。

## 蜕变关系19（适用部分测试用例，Set删除）

​	ftc的json文件将stc的json文件中列表中的最后一个元素删除，stc与ftc的JB完全一样，如果ftc的JB对象的集合实例添加删除的元素之后与stc的JB对象的集合实例不相等，该蜕变关系被违反。

## 蜕变关系20（适用部分测试用例，Set拆分）

ftc的json文件将stc的json文件中集合的元素均分到两个列表中，ftc的JB对象创建两个集合对象存放元素，如果ftc的JB对象中的两个集合实例的元素之和与stc的JB对象的集合实例中的元素不相等，该蜕变关系被违反。















