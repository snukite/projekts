import tkinter as tk

window = tk.Tk()
window.title("Informatīvā programma FISHING24-7 tirdzniecības automātiem")
window.geometry("1150x700")
window.resizable(False, False)
window.configure(bg="#e6f0cd")

sakuma_skats = tk.Frame(window,bg="#e6f0cd")
sakuma_skats.pack(fill='both', expand=True)
uzraksts = tk.Label(sakuma_skats, text="FISHING24-7", font=("Verdana", 30, "bold"), fg="#b90843", bg="#e6f0cd")
uzraksts.pack(pady=30)

window.mainloop()