## Linear Regression
### Concept of Linear Regression
![output](/linear_regression/linear_regression.png "Output")
<p>
    In regression, we want to predict continuous values whereas in classifications we want to predict a discrete value like a class label 0 or      1. So if we have a look at this example plot then we want to approximate this data with a linear function that's why it's called linear regression so we use a linear function to predict the values so we can define the approximation as 
</p><h4>Approximation</h4>
    
    ŷ = wx + b
    
<h4>Cost Function</h4>
<h6>Mean Square Error</h6>

![Mean square error.](/linear_regression/mse.jpg "Mean square error.")

<p>
    This is the error function. So we have to find the minimum of this function. We need it's to calculate the derivative or the gradient so we calculate the gradient of our cost function with respect to W and with respect to B. So this is the formula of the gradient.
</p>

![Cost Function](/linear_regression/cost.jpg "")

<p>
    With this gradient we use a technique that is called gradient descent so this is an iterative method to get to the minimum.
    if we have our object or our cost function here then we start somewhere so we have some initialization of 
</p>
<h4>Update Rules</h4>

h<sub>&theta;</sub>(x) = &theta;<sub>o</sub> x + &theta;<sub>1</sub>x

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}) 
