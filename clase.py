class Tickets:
    def __init__(self, codigo, patente, tipo_vehiculo, forma_pago, pais_cabina, distancia):
        self.codigo = codigo
        self.patente = patente
        self.tipo_vehiculo = tipo_vehiculo
        self.forma_pago = forma_pago
        self.pais_cabina = pais_cabina
        self.distancia = distancia

    def __str__(self):
        return "Codigo: " + str(self.codigo) + " " + "Patente: " + str(self.patente) + " " + "Tipo vehiculo: " + str(
            self.tipo_vehiculo) + " " + "Forma pago: " + str(self.forma_pago) + " " + "Pais cabina: " + str(
            self.pais_cabina) + " " + "Distancia: " + str(self.distancia)
