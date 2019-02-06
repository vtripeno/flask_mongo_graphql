# Graphene + MongoDb + Flask
Esta é apenas uma aplicação simples para demonstrar utilização de Flas, graphene e mongodb

Para executar a aplicação, use o comando:
```
python app.py
```


Para fazer uma Query de mutation, execute o seguinte comando:
```
mutation {
  createAll(employeeName: "teste", departmentName: "departamento teste", roleName: "role teste") {
    employee {
      name
      id
      hiredOn
      department {
        id
        name
      }
      role {
        id
        name
      }
    }
  }
}

```

Esta aplicação necessita de uma conexão com MongoDb

