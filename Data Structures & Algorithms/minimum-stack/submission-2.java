class MinStack {
    private Stack pile;
    private Stack minimumStack;
    int minimum;

    public MinStack() {
        pile = new Stack();
        minimumStack = new Stack();
        minimum = Integer.MAX_VALUE;
    }
    
    public void push(int val) {
        pile.push(val);
        if (minimum > val) {
            minimum = val;
        }
        minimumStack.push(minimum);
    }
    
    public void pop() {
        pile.pop();
        minimumStack.pop();
        if (minimumStack.isEmpty()) {
            minimum = Integer.MAX_VALUE;
        } else {
            minimum = (int) minimumStack.peek();
        }
    }
    
    public int top() {
        return (int) pile.peek();
    }
    
    public int getMin() {  
        return minimum;
    }
}
