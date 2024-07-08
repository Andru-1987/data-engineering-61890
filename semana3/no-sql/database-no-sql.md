- run code: 
```bash
# connection bash string 
mongosh --username root --password  --host "127.0.0.1" --port 27017

# Ver databases disponibles
show dbs
# seleccionar una BD
use data-storage
# verificar BD seleccionada
db
# Crear usuarios
db.createUser(
    {   "user":"andru",
        "pwd":"admin123",
        "roles":["readWrite","dbAdmin"]
    }
)

# Crear colecciones
db.createCollection('clientes');
show collections;

db.clientes.insert(
    {
        "nombres":"anderson",
        "apellido": "De Vega"
    }
)

db.clientes.insertMany([
    {
        "nombres": "Angel",
        "apellido": "MichellAngelo"
    },
    {
        "nombres": "Ana",
        "apellido": "García Pérez"
    },
    {
        "nombres": "Luis",
        "apellido": "Martínez López"
    },
    {
        "nombres": "María",
        "apellido": "Rodríguez Sánchez"
    }
]);


# ver registros de coleccion
db.clientes.find();
# ver de mejor manera
db.clientes.find().pretty();
```
