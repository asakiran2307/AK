import threading
import tkinter as tk
from tkinter import scrolledtext
from core.assistant import Assistant

class Dashboard:
    def __init__(self):
        self.root=tk.Tk(); self.root.title("AK // JARVIS"); self.root.geometry("1100x720")
        self.root.minsize(900,600); self.root.configure(bg="#070b12")
        self.assistant=Assistant(); self._build()

    def _build(self):
        tk.Label(self.root,text="AK // JARVIS",font=("Segoe UI",24,"bold"),fg="#62d9ff",bg="#070b12").pack(pady=(18,2))
        tk.Label(self.root,text="LOCAL AI  •  QWEN3 4B  •  OLLAMA",font=("Segoe UI",10),fg="#8493aa",bg="#070b12").pack()
        self.status=tk.Label(self.root,text="● ONLINE",fg="#65e6a0",bg="#070b12",font=("Segoe UI",10,"bold")); self.status.pack(pady=6)
        self.output=scrolledtext.ScrolledText(self.root,bg="#0c1320",fg="#dce8f5",insertbackground="white",font=("Consolas",11),wrap=tk.WORD,relief=tk.FLAT,padx=14,pady=14)
        self.output.pack(fill=tk.BOTH,expand=True,padx=24,pady=12)
        bar=tk.Frame(self.root,bg="#070b12"); bar.pack(fill=tk.X,padx=24,pady=(0,22))
        self.entry=tk.Entry(bar,bg="#111b2b",fg="white",insertbackground="white",font=("Segoe UI",12),relief=tk.FLAT)
        self.entry.pack(side=tk.LEFT,fill=tk.X,expand=True,ipady=11); self.entry.bind("<Return>",lambda _:self.send())
        tk.Button(bar,text="SEND",command=self.send,bg="#174a67",fg="white",relief=tk.FLAT,padx=22).pack(side=tk.RIGHT,padx=(10,0),ipady=8)
        tk.Button(bar,text="CLEAR",command=self.clear,bg="#202938",fg="white",relief=tk.FLAT,padx=16).pack(side=tk.RIGHT,padx=(8,0),ipady=8)
        self.write("AK","Online. Type a command to begin.")

    def write(self,who,message):
        self.output.insert(tk.END,f"\n[{who}]\n{message}\n"); self.output.see(tk.END)
    def clear(self): self.output.delete("1.0",tk.END)
    def send(self):
        text=self.entry.get().strip()
        if not text:return
        self.entry.delete(0,tk.END); self.write("YOU",text); self.status.config(text="● THINKING",fg="#ffd166")
        threading.Thread(target=self._worker,args=(text,),daemon=True).start()
    def _worker(self,text):
        try: result=self.assistant.respond(text)
        except Exception as exc: result=f"AK error: {exc}"
        self.root.after(0,lambda:self._done(result))
    def _done(self,result):
        self.write("AK",result); self.status.config(text="● ONLINE",fg="#65e6a0")
    def run(self):
        self.root.mainloop()
