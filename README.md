# Revolut expense manager

I'm building this simply because I store all my expenses in an excel file that's separated over multiple categories and subcategories and I'm tired of writing my expenses manually.

A sample file can be found in `./sample.xlsx`. Obviously those aren't my real expenses. The model comes from a financial advisor I was doing some meetings with, it's not designed by myself. I'd probably be too lazy to create one myself anyway.

I'll likely add some details on how I use the model in the future.

## Features

The app will support the following features:

- Add a new category, and a new sub-category for a category for a single sheet. Just having categories and subcategories is enough, I would spend too much time trying to find the best category hierarchy otherwise.
- Remove a category. This shall remove all subcategories.
- Remove a sub-category. This shall remove the category as a row, together with the price.
- Update the name of a category or sub-category.
- ...
