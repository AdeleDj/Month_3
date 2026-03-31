import tkinter as tk

def main():
    count = 0 

    def on_click():
        nonlocal count
        count += 1
        text_hello.config(text=f"Нажато: {count} раз")

    root = tk.Tk()
    root.title("Счётчик")

    text_hello = tk.Label(root, text="Нажато: 0 раз", font=("Arial", 14))
    text_hello.pack(pady=10)

    button = tk.Button(root, text="Нажми меня", command=on_click)
    button.pack(pady=10)

    root.mainloop()

main()