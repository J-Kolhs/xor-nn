from matrix import Matrix
import math

class NeuralNetwork:
    
    def __init__(self, inputs, hidden, output):
        self.num_inputs = inputs
        self.num_hidden = hidden
        self.num_output = output
    
        # Weights randomize    
        self.weights_ih = Matrix(self.num_hidden, self.num_inputs)
        self.weights_ho = Matrix(self.num_output, self.num_hidden)
        self.weights_ih.randomize()
        self.weights_ho.randomize()
        
        # Bias randomize
        self.bias_h = Matrix(self.num_hidden, 1) 
        self.bias_o = Matrix(self.num_output, 1)
        self.bias_h.randomize()
        self.bias_o.randomize()
        self.learning_rate = 0.1
        
    @staticmethod
    def sigmoid(x):
        return (1 / (1 + math.exp(-x)))
    
    @staticmethod
    def dsigmoid(y):
        return (y * (1-y))
    
    def feedforward(self, input_array):
        
        # Transform input array into inputs matrix
        inputs = Matrix.static_fromArray(input_array)
        
        # Generating the hidden layer
        hidden = Matrix.static_multiply(self.weights_ih, inputs)
        hidden.add(self.bias_h)
        hidden.map(self.sigmoid)
        
        # Generating the output layer
        output = Matrix.static_multiply(self.weights_ho, hidden)
        output.add(self.bias_o)
        output.map(self.sigmoid)
        
        # Return output array
        return Matrix.static_toArray(output)
        
    def train(self, input_array, target_array):
        
        # Transform input array into inputs matrix
        inputs = Matrix.static_fromArray(input_array)
        self.last_input = inputs
        
        # Generating the hidden layer
        hidden = Matrix.static_multiply(self.weights_ih, inputs)
        hidden.add(self.bias_h)
        hidden.map(self.sigmoid)

        # Generating the output layer
        output = Matrix.static_multiply(self.weights_ho, hidden)
        output.add(self.bias_o)
        output.map(self.sigmoid)
                      
        # Transform target array into target Matrix
        target = Matrix.static_fromArray(target_array)
        
        # 1. Calculate the errors
        ## a. Output errors
        output_errors = Matrix.static_substract(target, output)

        # 2. Calculate the gradient
        ## a. Output gradient (gradient of our output cost function)
        output_gradient = Matrix.static_map(output, self.dsigmoid)
        output_gradient.multiply(output_errors)

        
        # 3. Calculate the deltas adjustment
        ## a. Output deltas
        hidden_t = Matrix.static_transpose(hidden)
        weights_ho_delta = Matrix.static_multiply(output_gradient, hidden_t)
        weights_ho_delta.multiply(self.learning_rate)


        # 4. Adjust the original weights
        ## a. Output weights & output bias
        weights_ho = self.weights_ho
        self.weights_ho.add(weights_ho_delta)
        self.bias_o.add(output_gradient)
        
        # 1. Calculate the errors    
        ## b. Hidden layer errors
        who_t  = Matrix.static_transpose(self.weights_ho)
        hidden_errors = Matrix.static_multiply(who_t, output_errors)


        # 2. Calculate the gradient
        ## b. Hidden gradient (gradient of our hidden cost function)
        hidden_gradient = Matrix.static_map(hidden, self.dsigmoid)
        hidden_gradient = Matrix.static_map(hidden, self.dsigmoid)
        hidden_gradient.multiply(hidden_errors)     


        # 3. Calculate the deltas adjustment
        ## b. Hidden deltas
        inputs_t = Matrix.static_transpose(inputs)
        weights_ih_delta = Matrix.static_multiply(hidden_gradient, inputs_t)
        weights_ih_delta.multiply(self.learning_rate)
        self.weights_ih_delta = weights_ih_delta
        
        # 4. Adjust the original weights
        ## b. Biases weights & hidden bias
        self.weights_ih.add(weights_ih_delta)
        self.bias_h.add(hidden_gradient)