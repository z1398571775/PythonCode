import frida  #导入frida模块
import sys    #导入sys模块
 
jscode = """  
function get_func_addr(module, offset) {

   var base_addr = Module.findBaseAddress(module);
   console.log("base_addr: " + base_addr);

   console.log(hexdump(ptr(base_addr), {
            length: 16,
            header: true,
            ansi: true
        }))

   var func_addr = base_addr.add(offset);
   if (Process.arch == 'arm')
      return func_addr.add(1);  //如果是32位地址+1
   else
      return func_addr;
}

var func_addr = get_func_addr('libil2cpp.so', 0x9D5444);
console.log('func_addr: ' + func_addr);

console.log(hexdump(ptr(func_addr), {
            length: 16,
            header: true,
            ansi: true
        }))

Interceptor.attach(ptr(func_addr), {
   onEnter: function(args) {

      console.log("onEnter");
      var num1 = args[0];
      var num2 = args[1];

      console.log("num1: " + num1);
      console.log("num2: " + num2);

   },
   onLeave: function(retval) {

      console.log(retval);
      retval.replace(0x1);  //返回值替换成3
   }
});
"""
 
def on_message(message,data): #js中执行send函数后要回调的函数
    print(message)
 
process = frida.get_remote_device().attach('com.neowiz.game.guitargirl') #得到设备并劫持进程com.example.testfrida（该开始用get_usb_device函数用来获取设备，但是一直报错找不到设备，改用get_remote_device函数即可解决这个问题）
script = process.create_script(jscode) #创建js脚本
script.on('message',on_message) #加载回调函数，也就是js中执行send函数规定要执行的python函数
script.load() #加载脚本
sys.stdin.read()