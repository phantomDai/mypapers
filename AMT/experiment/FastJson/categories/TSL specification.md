# TSL specification

Parameters:

​		变量命名规则：

​					蛇形 

​					驼峰 

​					大驼峰

​		float：

​					不存在                                                   [property Empty]

​					存在，数值在精度范围                      [property NonEmpty]

​					不存在，数值不在精度范围              [property NonEmpty]

​		double：

​					不存在                                                    [if Empty]

​					存在，数值在精度范围                       [if NonEmpty]

​					不存在，数值不在精度范围               [if NonEmpty]

​		short：

​					不存在                                                    [if Empty]                                     

​					存在，数值在精度范围                       [if NonEmpty]

​					不存在，数值不在精度范围               [if NonEmpty]

​		byte：

​					不存在                                                    [if Empty] 

​					存在，数值在精度范围                       [if NonEmpty]

​					不存在，数值不在精度范围               [if NonEmpty]

​		int：

​					不存在                                                    [if Empty]

​					存在，数值在精度范围                       [if NonEmpty]

​					不存在，数值不在精度范围               [if NonEmpty]

​		long：

​					不存在                                                    [if Empty]

​					存在，数值在精度范围                       [if NonEmpty]

​					不存在，数值不在精度范围               [if NonEmpty]

​		boolean：

​					不存在                                                    [if Empty]

​					存在，数值在精度范围                       [if NonEmpty]

​		char:

​					不存在                                                    [if Empty]

​					存在，数值在精度范围                       [if NonEmpty]

​		date:

​					不存在

​					yyyy-MM-dd HH:mm:ss                    [property Exist]

​					yyyy/MM/dd HH:mm:ss                     [if Exist]

​					yyyy年M月d日 HH:mm:ss                  [if Exist]

​					yyyy年M月d日 H时m分s秒                 [if Exist]

​					yyyy년M월d일 HH:mm:ss                  [if Exist]

​					MM/dd/yyyy HH:mm:ss                      [if Exist]

​					dd/MM/yyyy HH:mm:ss                      [if Exist] 

​					dd.MM.yyyy HH:mm:ss                       [if Exist]

​					dd-MM-yyyy HH:mm:ss                      [if Exist]

​					yyyyMMdd                                              [if Exist]

​					yyyy/MM/dd                                           [if Exist]

​					yyyy年M月d日                                       [if Exist]

​					yyyy년M월d일                                       [if Exist]

​					MM/dd/yyyy                                          [if Exist]

​					dd/MM/yyyy                                          [if Exist]

​					dd.MM.yyyy                                          [if Exist]

​					dd-MM-yyyy                                         [if Exist]

​		string：

​					不存在

​					存在，小于80个字符

​					存在，大于80个字符

​		enum：

​					不存在

​					存在

​		map：

​					不存在                              [if Empty]

​					HashMap                          [if NonEmpty] [property hasHashMap]

​					LinkedHashMap              [if NonEmpty] [property hasLinkedMap]

​					dentityHashMap              [if NonEmpty]

​		list：

​					不存在                                 [if Empty]

​					ArrayList                             [if NonEmpty and hasHashMap]

​					LinkedList                           [if NonEmpty and hasLinkedMap]

​		set：

​					不存在                                   [if Empty]

​					HashSet                                 [if NonEmpty and hasHashMap]

​					LinkedHashSet                     [if NonEmpty and hasLinkedMap]