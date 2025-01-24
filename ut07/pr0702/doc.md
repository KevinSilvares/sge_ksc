# PR0702: API REST

En esta práctica se hace una API Rest en Odoo con el módulo de suscripciones.

## Fichero controllers

__Primera parte:__ Permite introducir parámetros para buscar por el estado (_status_).

```python
 @http.route('/api/subscription', type='http', auth='none', csrf=False, methods=['GET'])
    def get_subs_by_status(self):
        try:
            possible_status = ('active', 'cancelled', 'pending', 'expired')
            estado = request.params.get('estado')
            if estado not in possible_status:
                return Response(
                        json.dumps({'msg': 'Estado no válido. Prueba con: active, cancelled, pending o expired.'}),
                        content_type = "application/json",
                        status = 404,
                    )
            
            if estado:
                subs = request.env['subscription.subscription'].sudo().search([('status', '=', estado)])
                if not subs:
                    return Response(
                        json.dumps({'msg': 'No se encontraron registros.'}),
                        content_type = "application/json",
                        status = 404,
                    )
            
                data = []
                for sub in subs:
                    sub_dic = {
                    'name' : sub.name,
                    'subscription_code' : sub.subscription_code,
                    'start_date' : str(sub.start_date),
                    'end_date' : str(sub.end_date),
                    'duration_months' : sub.duration_months,
                    'renewal_date' : str(sub.renewal_date),
                    'status' : sub.status,
                    'is_renewable' : sub.is_renewable,
                    'price' : sub.price
                    }
                    data.append(sub_dic)

                return Response(
                    json.dumps(data),
                    content_type = "application/json",
                    status = 200
                )
        except Exception as e:
            return Response(
                json.dumps({'msg' : f"Error intenrno del servidor: {str(e)}"}),
                content_type = "application/json",
                status = 500
            )
```
## Funcionamiento

__URL:__ http://localhost:8069/api/subscription?estado=active

![Petición con párametro](image.png)
Petición con párametro exitosa.

![Petición con párametro fallida](image-1.png)
Petición con párametro fallida.

__Segunda parte:__ Permite introducir valores a la URL base un parámetro.

__URL__: http://localhost:8069/api/subscription/Anacleto


```python
    @http.route('/api/subscription/<string:name>', type='http', methods = ['GET'], csrf=False)
    def get_sub_by_name(self, name):
        try:
            sub = request.env['subscription.subscription'].sudo().search([('name', '=', name)], limit=1)
            if not sub:
                return Response(
                    json.dumps({'msg' : 'Datos no encontrados'}),
                    content_type = "application/json",
                    status = 404
                ) 
            
            data = {
                'name' : sub.name,
                'subscription_code' : sub.subscription_code,
                'start_date' : str(sub.start_date),
                'end_date' : str(sub.end_date),
                'duration_months' : sub.duration_months,
                'renewal_date' : str(sub.renewal_date),
                'status' : sub.status,
                'is_renewable' : sub.is_renewable,
                'price' : sub.price
            }

            return Response(
                json.dumps(data),
                content_type = "application/json",
                status = 200
            )
        except Exception as e:
            return Response(
                json.dumps({'msg' : f"Error intenrno del servidor: {str(e)}"}),
                content_type = "application/json",
                status = 500
            )
```

## Funcionamiento

![Petición exitosa](image-2.png)
Petición exitosa.

![Petición fallida](image-3.png)
Petición fallida.