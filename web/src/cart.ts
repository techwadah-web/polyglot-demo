export interface CartLine {
  isbn: string;
  title: string;
  unitPrice: number;
  quantity: number;
}

export class Cart {
  private lines: CartLine[] = [];

  add(line: CartLine): void {
    const existing = this.lines.find((l) => l.isbn === line.isbn);
    if (existing) {
      existing.quantity += line.quantity;
    } else {
      this.lines.push({ ...line });
    }
  }

  remove(isbn: string): void {
    this.lines = this.lines.filter((l) => l.isbn !== isbn);
  }

  subtotal(): number {
    return this.lines.reduce((sum, l) => sum + l.unitPrice * l.quantity, 0);
  }
}

export function formatPrice(amount: number, currency = "USD"): string {
  return new Intl.NumberFormat("en-US", { style: "currency", currency }).format(amount);
}
