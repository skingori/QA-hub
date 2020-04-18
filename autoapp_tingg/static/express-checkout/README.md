# Express Checkout JavaScript Library
This is the easiest way for merchants to integrate Tingg's checkout functionality on their online platform. This library exposes a javascript object ```Tingg``` with two helper functions:
+ renderPayButton
+ renderCheckout

## Usage
#### 1. Adding the checkout button
```javascript
Tingg.renderPayButton({
    text: '',
    color: '',
    className: ''
})
```

Tingg.renderPayButton(```{options}```)
| option      | values                                                      | type                             | required                                 
|-------------|-------------------------------------------------------------|----------------------------------|------------------------------------------
| text        | any                                                         | ```String```                     | ```FALSE```                              
| color       | 'red', 'blue', 'pink', 'black', 'green', 'yellow', 'purple' | ```String```, ```Number```       | ```FALSE```                              
| className   | any                                                         | ```String```                     | ```TRUE```                               

#### 2. Render the appropriate checkout page view
```javascript
Tingg.renderCheckout({
    type: '',
    payload: {
        params: '',
        accessKey: '',
        countryCode: ''
    },
})
```

Tingg.renderCheckout(```{options}```)
| option                | values                                                                        | type          | required  
|-----------------------|-------------------------------------------------------------------------------|---------------|-----------
| payload               | { params: ```String```, accessKey: ```String```, countryCode: ```String```}   | ```Object```  | ```TRUE```
| type                  | 'modal', 'redirect'                                                           | ```String```  | ```TRUE```
