from seminar10.flight import Flight
from seminar10.validator import FlightValidator
from seminar10.repository import Repository
from seminar10.service import Service
from seminar10.ui import UI


if __name__ == "__main__":
    repo = Repository("")
    service = Service(repo, FlightValidator())
    ui = UI(service)
    ui.main()
