
## [2.0.0] - 2019-09-25
### Added
- New brand identity by [Tingg](https://tingg.africa/).
- Added feature to customize button text by adding a text key to the param object
    ```
    Tingg.renderPayButton({
        text: ''
    })
    ```
- Added feature to customize button color by adding a color key to the param object
    ```
    Tingg.renderPayButton({
        color: ''
    })
    ```
    Theme   | Colour  
    --------|---------
    red     | #F65058 
    blue    | #6CD1EF 
    pink    | #F984CA 
    black   | #0D171A 
    green   | #3BD23D 
    yellow  | #FFC915 
    purple  | #5D538B 

### Changed
- Function to add checkout button to DOM

    use ```Tingg.renderPayButton()``` instead of ```Tingg.addPayWithTinggButton()```
- Function to create a checkout request

    use ```Tingg.renderCheckout()``` instead of ```Tingg.renderTinggCheckout()```

- Express checkout type naming from **express** to **redirect**