'''
装饰器允许我们将一个提供核心功能的对象和其他可以改变这个功能的对象“包裹”在一起。
也就是说，装饰对象的接口与核心对象相同。
装饰器的两大用途：
    增加一个组件向另一个组件发送数据时的响应能力。
    支持多种可选行为。
    
    
观察者模： 应用于状态监测和事件处理等场景
    这种模式确保一个核心对象可以由一组未知并可能正在扩展的"观察者"对象来监控。
    
策略模式： 
    连接到策略模式的用户代码仅仅需要知道和它打交道的抽象接口。
    
状态模式：
    状态模式的目的是实现状态转换系统：
    对象显而易见地处于一个特定状态，同时某些活动可能驱动它转变到另一个不同的状态。
    为了实现这个目的，我们需要一个管理者类或上下文类为状态转换提供一个接口。
    在内部，这个类包含一个指向当前状态的指针；
    每个状态都知道可以转换为哪些其他状态并如何根据调用的操作转换为哪些其他状态并如何根据调用的操作转换到这个状态。

单例模式：
    基本理念是允许一些对象只存在一个实例。
'''