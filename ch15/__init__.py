'''
字典推导
setdefault处理找不到的键
defaultdict: 处理找不到的键的一个选择
__getitem__找不到的键的时候被调用，让__getitem__返回某种默认值。
特殊方法__missing__，那么在__getitem__碰到找不到的时候，python会自动调用它
不可变映射类型
types模块中引入一个封装类名叫MappingProxyType
如果给这个类一个映射，它就会返回一个只读的映射视图，但是它是动态的。


集合的本质是许多唯一对象的聚集。
'''