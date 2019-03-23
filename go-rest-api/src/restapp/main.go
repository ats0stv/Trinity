package main

import (
	"log"
	"net/http"
	"controllers/personcontroller"
	"setup"
)


func main() {
	log.Print("Init Test ReST Application")
	
	log.Print("Adding Fake Data")
	personcontroller.AddDummyPeople()

	log.Print("Configuring Routes")
	router := setup.ConfigureRoutes()

	log.Print("Starting Server")
	log.Fatal(http.ListenAndServe(":11223", router))
}

