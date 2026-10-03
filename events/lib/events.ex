defmodule Events do
  @moduledoc "Append-only log of order events."

  def new, do: []

  def record(log, type, order_id) do
    [%{type: type, order_id: order_id} | log]
  end

  def for_order(log, order_id) do
    Enum.filter(log, &(&1.order_id == order_id))
  end
end
