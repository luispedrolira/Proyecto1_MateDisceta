import tkinter as tk
from tkinter import simpledialog, messagebox
from Operations import Operations  
from Set import Set  

class SetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Operaciones de Conjuntos")
        self.sets = {}  # Diccionario para almacenar conjuntos
        self.operations = None  # Inicializamos como None, se asignará en `operate_sets`

        # Menú principal
        self.main_menu = tk.Frame(root)
        self.main_menu.pack()

        self.build_button = tk.Button(self.main_menu, text="Construir Conjuntos", command=self.build_sets)
        self.build_button.pack(pady=10)

        self.operate_button = tk.Button(self.main_menu, text="Operar Conjuntos", command=self.operate_sets)
        self.operate_button.pack(pady=10)

        self.exit_button = tk.Button(self.main_menu, text="Finalizar", command=root.quit)
        self.exit_button.pack(pady=10)

        # Área de texto para mostrar resultados
        self.result_label = tk.Label(self.main_menu, text="Resultado de la Operación:")
        self.result_label.pack(pady=5)

        self.result_text = tk.Text(self.main_menu, height=5, width=50)
        self.result_text.pack(pady=5)
        self.result_text.config(state=tk.DISABLED)

    def build_sets(self):
        set_name = simpledialog.askstring("Nombre del Conjunto", "Ingrese un nombre para el conjunto:")
        if set_name:
            if set_name in self.sets:
                messagebox.showerror("Error", "El nombre del conjunto ya existe. Por favor, elija otro nombre.")
            else:
                new_set = self.input_set(set_name)
                if new_set:
                    self.sets[set_name] = new_set
                    messagebox.showinfo("Información", f"El conjunto '{set_name}' ha sido creado exitosamente.")
        else:
            messagebox.showwarning("Advertencia", "Debe ingresar un nombre para el conjunto.")

    def input_set(self, set_name):
        elements = simpledialog.askstring("Construir Conjunto", f"Ingrese los elementos del {set_name} (A-Z, 0-9):")
        new_set = Set()
        if elements:
            for element in elements.upper():
                if element.isalnum() and element in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
                    new_set.add_element(element)
                else:
                    messagebox.showwarning("Advertencia", f"El elemento '{element}' es inválido y será ignorado.")
        return new_set

    def operate_sets(self):
        if len(self.sets) < 2:
            messagebox.showwarning("Advertencia", "Debe crear al menos dos conjuntos para realizar operaciones.")
            return

        set1_name = simpledialog.askstring("Seleccionar Conjunto 1", f"Ingrese el nombre del primer conjunto (disponibles: {', '.join(self.sets.keys())}):")
        set2_name = simpledialog.askstring("Seleccionar Conjunto 2", f"Ingrese el nombre del segundo conjunto (disponibles: {', '.join(self.sets.keys())}):")
        
        if set1_name in self.sets and set2_name in self.sets:
            set1 = self.sets[set1_name]
            set2 = self.sets[set2_name]

            # Se pasa el primer conjunto (set1) al crear la instancia de Operations
            self.operations = Operations(set1)

            operation = simpledialog.askstring("Operar Conjuntos", "Ingrese la operación (Complemento, Unión, Intersección, Diferencia, Diferencia Simétrica):")
            
            if operation:
                operation = operation.lower()
                result = None

                if operation == "complemento":
                    result = self.operations.complement()
                elif operation == "unión":
                    result = self.operations.union(set2)
                elif operation == "intersección":
                    result = self.operations.intersection(set2)
                elif operation == "diferencia":
                    result = self.operations.difference(set2)
                elif operation == "diferencia simétrica":
                    result = self.operations.symmetric_difference(set2)
                else:
                    messagebox.showerror("Error", "Operación no válida.")
                    return

                # Mostrar el resultado en la interfaz gráfica
                self.show_result(operation.capitalize(), result, set1_name, set2_name)
        else:
            messagebox.showerror("Error", "Uno o ambos nombres de conjuntos no son válidos.")

    def show_result(self, operation_name, result, set1_name, set2_name):
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Operación: {operation_name} entre '{set1_name}' y '{set2_name}'\n")
        self.result_text.insert(tk.END, f"Resultado: {result}\n")
        self.result_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = SetApp(root)
    root.mainloop()
