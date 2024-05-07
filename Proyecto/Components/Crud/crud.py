class CRUD:
    @staticmethod
    def buscar_factura_por_fecha(facturas, fecha):
        for factura in facturas:
            if factura["fecha"] == fecha:# Comprueba si la fecha de la factura actual coincide con la fecha buscada.
                return factura # Retorna la factura si se encuentra.
            return None # Retorna None si no se encuentra ninguna factura con la fecha especificada.
        
    
    def buscar_facturas_por_cedula(facturas, cedula_cliente):# Método para buscar todas las facturas asociadas a un cliente por su cédula.
        facturas_cliente = [] # Inicializa una lista para almacenar las facturas del cliente.
        for factura in facturas: # Itera sobre cada factura en la lista.
            if factura.get("cedula_cliente") == cedula_cliente:# Comprueba si la cédula del cliente de la factura actual coincide con la cédula buscada.
                facturas_cliente.append(factura) # Agrega la factura a la lista de facturas del cliente.
                return facturas_cliente
        

    @staticmethod
    def eliminar_factura_por_fecha(facturas, fecha):
        for factura in facturas:
            if factura["fecha"] == fecha:# Comprueba si la fecha de la factura actual coincide con la fecha buscada.
                facturas.remove(factura)  # Elimina la factura de la lista.
                return True  # Retorna True para indicar que se eliminó una factura.
            return False # Retorna False si no se encontró ninguna factura con la fecha especificada.
        

    @staticmethod
    def modificar_valor_factura_por_fecha(facturas, fecha, nuevo_valor):
        for factura in facturas:
            if factura["fecha"] == fecha:  # Comprueba si la fecha de la factura actual coincide con la fecha buscada.
                factura["valor_total"] = nuevo_valor  # Modifica el valor total de la factura actual con el nuevo valor especificado.
                return True # Retorna True para indicar que se modificó el valor de una factura.
            return False       # Retorna False si no se encontró ninguna factura con la fecha especificada.
  
