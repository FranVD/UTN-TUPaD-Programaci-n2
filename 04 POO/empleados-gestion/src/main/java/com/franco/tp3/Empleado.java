/* REYNOSO ARELLANO, FRANCO GASTON.
1. Implementar la clase Empleado aplicando todos los puntos anteriores.
2. Crear una clase de prueba con método main que:
*/

package com.franco.tp3;

public class Empleado {

    private int id;
    private String nombre;
    private String puesto;
    private double salario;

    private static int totalEmpleados = 0;
    private static int siguienteId = 1;

    public Empleado(int id, String nombre, String puesto, double salario) {
        this.id = id;
        this.nombre = nombre;
        this.puesto = puesto;
        this.salario = salario;
        totalEmpleados++;
        if (id >= siguienteId) {
            siguienteId = id + 1;
        }
    }

    public Empleado(String nombre, String puesto) {
        this.id = siguienteId++;
        this.nombre = nombre;
        this.puesto = puesto;
        this.salario = 0.0;
        totalEmpleados++;
    }

    public void actualizarSalario(double porcentaje) {
        if (porcentaje != 0) {
            this.salario += this.salario * (porcentaje / 100.0);
        }
    }

    public void actualizarSalario(int cantidadFija) {
        this.salario += cantidadFija;
    }

    @Override
    public String toString() {
        return "Empleado{id=" + id +
               ", nombre='" + nombre + ''' +
               ", puesto='" + puesto + ''' +
               ", salario=" + String.format("%.2f", salario) +
               '}';
    }

    public static int mostrarTotalEmpleados() {
        return totalEmpleados;
    }

    public int getId() { return id; }
    public void setId(int id) { this.id = id; }
    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }
    public String getPuesto() { return puesto; }
    public void setPuesto(String puesto) { this.puesto = puesto; }
    public double getSalario() { return salario; }
    public void setSalario(double salario) { if (salario >= 0) this.salario = salario; }
}
