# Sends order notifications to customers.
module Notify
  class Mailer
    def initialize(sender)
      @sender = sender
    end

    def order_confirmed(email, order_id)
      deliver(email, "Order #{order_id} confirmed")
    end

    def order_shipped(email, order_id, tracking)
      deliver(email, "Order #{order_id} shipped: #{tracking}")
    end

    private

    def deliver(to, subject)
      @sender.call(to: to, subject: subject)
    end
  end
end
