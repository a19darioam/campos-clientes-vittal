BASE_XML="""
<?xml version="1.0" encoding="UTF-8"?><soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:scfd="http://namespace.pegasotecnologia.com/SCFD" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/">
    <soapenv:Header></soapenv:Header>
    <soapenv:Body>
        <scfd:emitirCFD>
            <scfd:PoRequestCFD>
                <RequestCFD version="3.3">
                    <Comprobante Version="3.3" Serie="VD" Folio="833" Fecha="2020-06-26T11:33:04" FormaPago="03" SubTotal="6000.05" Moneda="MXN" Total="6000.05" TipoDeComprobante="I" MetodoPago="PUE" LugarExpedicion="15900">
                        <Emisor Rfc="TMO1104114Y9" Nombre="TIEMPOREAL_TMO1104114Y9_ws" RegimenFiscal="601"/>
                        <Receptor Rfc="RIMJ7108165N0" Nombre="RIVERO MERCADO JUAN MANUEL" UsoCFDI="P01"/>
                        <Conceptos>
                            <Concepto ClaveProdServ="43232605" Cantidad="1." ClaveUnidad="48" Unidad="1" Descripcion="Servicio Medico" ValorUnitario="6000.05" Importe="6000.05"/>
                        </Conceptos>
                    </Comprobante>
                    <Transaccion id="20180420132024"/>
                    <TipoComprobante clave="Factura" nombre="Factura"/>
                    <Sucursal nombre="MATRIZ"/>
                    <Receptor emailReceptor="juanmanuelriverom@gmail.com"/>{}
                </RequestCFD>
            </scfd:PoRequestCFD>
        </scfd:emitirCFD>
    </soapenv:Body>
</soapenv:Envelope>"""

print(BASE_XML.format('hello!!!!!'))