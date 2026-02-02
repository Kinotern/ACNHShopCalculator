import tkinter as tk
from tkinter import ttk

class IntegerConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("动森整数转换器")
        self.root.geometry("450x250")
        self.root.resizable(False, False)
        
        # 设置窗口置顶
        self.root.attributes('-topmost', True)
        
        # 窗口居中
        self.center_window()
        
        # 设置样式
        style = ttk.Style()
        style.theme_use('clam')
        
        # 创建主框架
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 标题
        title_label = ttk.Label(
            main_frame, 
            text="动森负数转换工具",
            font=("Arial", 16, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # 说明文本
        explanation_text = "输入负数，获取对应的负数菜价"
        explanation_label = ttk.Label(
            main_frame, 
            text=explanation_text,
            font=("Arial", 10)
        )
        explanation_label.grid(row=1, column=0, columnspan=2, pady=(0, 15))
        
        # 输入部分
        input_frame = ttk.Frame(main_frame)
        input_frame.grid(row=2, column=0, columnspan=2, pady=(0, 15))
        
        # 固定"负"字
        ttk.Label(input_frame, text="负", font=("Arial", 16, "bold")).grid(row=0, column=0, padx=(0, 5))
        
        # 输入框
        self.input_var = tk.StringVar()
        self.input_entry = ttk.Entry(
            input_frame, 
            textvariable=self.input_var, 
            width=20,
            font=("Arial", 14),
            justify='right'
        )
        self.input_entry.grid(row=0, column=1, padx=(0, 10))
        
        # 转换按钮
        self.convert_button = ttk.Button(
            input_frame, 
            text="转换", 
            command=self.convert,
            width=8
        )
        self.convert_button.grid(row=0, column=2)
        
        # 绑定回车键
        self.root.bind('<Return>', lambda e: self.convert())
        
        # 结果标签
        result_label = ttk.Label(
            main_frame,
            text="对应的菜价为：",
            font=("Arial", 10)
        )
        result_label.grid(row=3, column=0, columnspan=2, pady=(10, 5))
        
        # 结果展示
        self.result_var = tk.StringVar()
        self.result_var.set("等待输入...")
        
        result_display = ttk.Label(
            main_frame,
            textvariable=self.result_var,
            font=("Courier", 14, "bold"),
            background="#f0f0f0",
            relief="solid",
            padding=10,
            width=25
        )
        result_display.grid(row=4, column=0, columnspan=2, pady=(0, 10))
        
        # 示例部分
        example_frame = ttk.Frame(main_frame)
        example_frame.grid(row=5, column=0, columnspan=2, pady=(10, 0))
        
        ttk.Label(example_frame, text="示例：", font=("Arial", 9)).grid(row=0, column=0, sticky=tk.W)
        
        examples = ["负1 → 4294967295", "负2 → 4294967294", "负3 → 4294967293"]
        
        for i, example in enumerate(examples):
            ttk.Label(
                example_frame, 
                text=example, 
                font=("Arial", 9),
                foreground="gray"
            ).grid(row=0, column=i+1, padx=(10, 0))
        
        # 提示文字
        tip_label = ttk.Label(
            main_frame,
            text="提示：输入数字后按回车键或点击转换按钮",
            font=('Arial', 8),
            foreground="gray"
        )
        tip_label.grid(row=6, column=0, columnspan=2, pady=(10, 0))
        
        # 软件信息
        info_label = ttk.Label(
            main_frame,
            text="本软件免费！Kinotern制作",
            font=('Arial', 8),
            foreground="gray"
        )
        info_label.grid(row=7, column=0, columnspan=2, pady=(5, 0))
        
        # 聚焦到输入框
        self.input_entry.focus()
    
    def convert(self):
        """执行转换"""
        try:
            input_str = self.input_var.get().strip()
            
            if not input_str:
                self.result_var.set("请输入数字")
                return
            
            # 将输入转换为整数（负数）
            try:
                # 用户只需要输入数字部分，我们自动加上负号
                input_num = -abs(int(input_str))
            except ValueError:
                self.result_var.set("请输入有效的数字")
                return
            
            # 执行转换：有符号负数转无符号32位整数
            # 优化算法：直接计算 2^32 + input_num
            # 因为 input_num 是负数，所以相当于 4294967296 - abs(input_num)
            unsigned_num = 4294967296 + input_num
            
            # 显示结果
            self.result_var.set(str(unsigned_num))
            
            # 自动选中结果文本，方便复制
            self.root.clipboard_clear()
            self.root.clipboard_append(str(unsigned_num))
            
        except Exception as e:
            self.result_var.set(f"错误: {str(e)}")
    
    def clear_input(self):
        """清空输入"""
        self.input_var.set("")
        self.result_var.set("等待输入...")
        self.input_entry.focus()
    
    def center_window(self):
        """窗口居中"""
        # 获取窗口尺寸
        window_width = 450
        window_height = 250
        
        # 获取屏幕尺寸
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # 计算居中位置
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        # 设置窗口位置
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

def show_welcome_popup():
    """显示欢迎弹窗"""
    # 创建弹窗
    popup = tk.Tk()
    popup.title("欢迎")
    popup.geometry("300x180")
    popup.resizable(False, False)
    popup.attributes('-topmost', True)
    
    # 弹窗居中
    popup_width = 300
    popup_height = 180
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    x = (screen_width - popup_width) // 2
    y = (screen_height - popup_height) // 2
    popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")
    
    # 创建弹窗内容
    frame = ttk.Frame(popup, padding="30")
    frame.pack(fill=tk.BOTH, expand=True)
    
    # 标题
    title_label = ttk.Label(
        frame, 
        text="欢迎使用动森负数转换工具",
        font=("Arial", 12, "bold")
    )
    title_label.pack(pady=(0, 15))
    
    # 信息
    info_label = ttk.Label(
        frame, 
        text="本工具完全免费\n由Kinotern制作",
        font=("Arial", 10),
        justify='center'
    )
    info_label.pack(pady=(0, 20))
    
    # 确认按钮
    def on_ok():
        popup.destroy()
        # 显示主窗口
        root = tk.Tk()
        app = IntegerConverterApp(root)
        root.mainloop()
    
    ok_button = ttk.Button(
        frame, 
        text="确认", 
        command=on_ok,
        width=10
    )
    ok_button.pack()
    
    # 运行弹窗
    popup.mainloop()

def main():
    # 先显示欢迎弹窗
    show_welcome_popup()

if __name__ == "__main__":
    main()