class CRUD:
    @staticmethod
    def buscar_factura_por_fecha(facturas, fecha):
        for factura in facturas:
            if factura["fecha"] == fecha:
                return factura
            return None 
        
    
    def buscar_facturas_por_cedula(facturas, cedula_cliente):
        facturas_cliente = [] 
        for factura in facturas: 
            if factura.get("cedula_cliente") == cedula_cliente:
                facturas_cliente.append(factura) 
                return facturas_cliente
        

    @staticmethod
    def eliminar_factura_por_fecha(facturas, fecha):
        for factura in facturas:
            if factura["fecha"] == fecha:
                facturas.remove(factura) 
                return True  
            return False 
        

    @staticmethod
    def modificar_valor_factura_por_fecha(facturas, fecha, nuevo_valor):
        for factura in facturas:
            if factura["fecha"] == fecha:  
                factura["valor_total"] = nuevo_valor  
                return True
            return False       
  
