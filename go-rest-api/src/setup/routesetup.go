package setup

import (
	"log"
	"github.com/gorilla/mux"
	"controllers/personcontroller"
)

func ConfigureRoutes() *mux.Router {
	router := mux.NewRouter()
	log.Print("Adding People routes to the router")
	configurePeopleRoutes(router)

    log.Print("Completed Route Mapping to Controllers")
    return router
}

func configurePeopleRoutes(router *mux.Router) {
	router.HandleFunc("/people", personcontroller.GetPeople).Methods("GET")
    router.HandleFunc("/people/{id}", personcontroller.GetPerson).Methods("GET")
    router.HandleFunc("/people/{id}", personcontroller.CreatePerson).Methods("POST")
    router.HandleFunc("/people/{id}", personcontroller.DeletePerson).Methods("DELETE")
}