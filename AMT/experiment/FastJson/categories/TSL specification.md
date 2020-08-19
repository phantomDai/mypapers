# TSL specification

Parameters:

​		变量命名规则：

​					蛇形 

​					驼峰 

​					大驼峰

​		float：

​					不存在                                                   [property Empty]

​					存在，数值在精度范围                      [property NonEmpty]

​					存在，数值不在精度范围                 [property NonEmptyOut]

​		double：

​					不存在                                                    [if Empty]

​					存在，数值在精度范围                       [if NonEmpty]

​					存在，数值不在精度范围                   [if NonEmptyOut]

​		short：

​					不存在                                                    [if Empty]                                     

​					存在，数值在精度范围                       [if NonEmpty]

​					存在，数值不在精度范围               [if NonEmptyOut]

​		byte：

​					不存在                                                    [if Empty] 

​					存在，数值在精度范围                       [if NonEmpty]

​					存在，数值不在精度范围                   [if NonEmptyOut]

​		int：

​					不存在                                                    [if Empty]

​					存在，数值在精度范围                       [if NonEmpty]

​					存在，数值不在精度范围                   [if NonEmptyOut]

​		long：

​					不存在                                                    [if Empty]

​					存在，数值在精度范围                       [if NonEmpty]

​					存在，数值不在精度范围                   [if NonEmptyOut]

​		boolean：

​					不存在                                                    

​					存在                                                        

​		char:

​					不存在                                                    

​					存在，数值在精度范围                       

​		date:

​					不存在

​					 存在

​					yyyy-MM-dd HH:mm:ss                    

​					yyyy/MM/dd HH:mm:ss                     

​					yyyy年M月d日 HH:mm:ss                  

​					yyyy年M月d日 H时m分s秒                 

​					yyyy년M월d일 HH:mm:ss                  

​					MM/dd/yyyy HH:mm:ss                      

​					dd/MM/yyyy HH:mm:ss                      

​					dd.MM.yyyy HH:mm:ss                       

​					dd-MM-yyyy HH:mm:ss                      

​					yyyyMMdd                                              

​					yyyy/MM/dd                                           

​					yyyy年M月d日                                       

​					yyyy년M월d일                                       

​					MM/dd/yyyy                                          

​					dd/MM/yyyy                                          

​					dd.MM.yyyy                                          

​					dd-MM-yyyy                                         

​		string：

​					不存在

​					存在，小于80个字符

​					存在，大于80个字符

​		enum：

​					不存在

​					存在

​		map：

​					不存在                              

​					HashMap                          [property hasHashMap]

​					LinkedHashMap              [property hasLinkedMap]

​					dentityHashMap              

​		list：

​					不存在                                 

​					ArrayList                             

​					LinkedList                           [if hasLinkedMap]

​		set：

​					不存在                                   [if Empty]

​					HashSet                                 [hasHashMap]

​					LinkedHashSet                     [hasLinkedMap]