mutation {
  createEmployee(name: "TESTE") {
    employee {
      name
      id
    }
  }
}


python app.py