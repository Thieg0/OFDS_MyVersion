# support.py
class Support:
    def __init__(self):
        self._tickets = []

    def open_ticket(self, customer_id, issue):
        ticket = {
            "customer_id": customer_id,
            "issue": issue,
            "status": "Aberto",
            "response": None
        }
        self._tickets.append(ticket)
        return f"Ticket aberto: {issue}"

    def respond_to_ticket(self, ticket_index, response):
        if 0 <= ticket_index < len(self._tickets):
            self._tickets[ticket_index]["response"] = response
            self._tickets[ticket_index]["status"] = "Fechado"
            return f"Ticket {ticket_index} respondido e fechado."
        else:
            raise ValueError("Ticket não encontrado.")

    def display_tickets(self):
        return "\n".join([f"Ticket {i}: {ticket['issue']} (Status: {ticket['status']}, Resposta: {ticket['response']})"
                          for i, ticket in enumerate(self._tickets)])
