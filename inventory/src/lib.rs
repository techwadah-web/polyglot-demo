use std::collections::HashMap;

#[derive(Debug, Clone, PartialEq)]
pub struct Book {
    pub isbn: String,
    pub title: String,
    pub stock: u32,
}

#[derive(Debug, PartialEq)]
pub enum StockError {
    UnknownBook,
    OutOfStock { available: u32 },
}

#[derive(Default)]
pub struct Inventory {
    books: HashMap<String, Book>,
}

impl Inventory {
    pub fn add(&mut self, book: Book) {
        self.books.insert(book.isbn.clone(), book);
    }

    pub fn reserve(&mut self, isbn: &str, quantity: u32) -> Result<u32, StockError> {
        let book = self.books.get_mut(isbn).ok_or(StockError::UnknownBook)?;
        if book.stock < quantity {
            return Err(StockError::OutOfStock { available: book.stock });
        }
        book.stock -= quantity;
        Ok(book.stock)
    }

    pub fn restock(&mut self, isbn: &str, quantity: u32) -> Result<u32, StockError> {
        let book = self.books.get_mut(isbn).ok_or(StockError::UnknownBook)?;
        book.stock += quantity;
        Ok(book.stock)
    }
}
