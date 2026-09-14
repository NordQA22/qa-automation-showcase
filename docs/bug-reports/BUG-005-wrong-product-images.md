# BUG-005: All products show the same image for problem_user

## Summary
On the Products page, all six products display the same image — the image of "Sauce Labs Backpack" — instead of their own distinct product photos.

## Environment
- **URL:** https://www.saucedemo.com/inventory.html
- **User:** `problem_user` / `secret_sauce`

## Steps to Reproduce
1. Log in as `problem_user`
2. On the Products page, observe the product images

## Expected Result
Each product has its own unique image matching the product name.

## Actual Result
All six products show the same image (Sauce Labs Backpack).

## Severity
**Major**

## Priority
**Medium**

## Attachments

![Screenshot](screenshots/bug-005-wrong-images.png)