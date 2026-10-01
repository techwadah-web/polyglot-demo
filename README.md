# polyglot-demo

A small bookstore order system written in several languages, used to
demonstrate [Wadah](https://wadah.tech). The code is intentionally simple.
What matters is the mix of languages and the commit history.

| Folder | Language | Wadah support |
|---|---|---|
| `inventory/` | Rust | see `wadah knowledge capabilities` |
| `pricing/` | Python | needs `python3` |
| `api/` | Go | needs `go` |
| `web/` | TypeScript | |
| `billing/` | Java | |
| `notify/` | Ruby | |
| `events/` | Elixir | |

## Try it

```bash
git clone https://github.com/techwadah-web/polyglot-demo
cd polyglot-demo
wadah doctor
wadah analyze
wadah learn
wadah knowledge capabilities --analyze
wadah knowledge symbols --query reserve --json
```

## History

Each commit shows one kind of change Wadah can report:

1. Initial inventory, pricing and API (Rust, Python, Go)
2. Add web cart and billing (TypeScript, Java)
3. Add notifications and event log (Ruby, Elixir)
4. Lines move, nothing else changes (inventory doc comments)
5. A signature changes (`apply_discount` takes a customer tier)
6. A rename (`Cart.total` becomes `Cart.subtotal`, `mailer.rb` becomes `email.rb`)

Compare any two of them with `wadah delta` and
`wadah knowledge symbol-deltas`.

## License

Apache-2.0
