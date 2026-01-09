#  Day 9 Infinite Memory(Generators) 
## Goals:
1. Yield is used to utilize memory efficiently.Unlike return ,it doesn't return the entire output at once.Instand, yield pauses the function execution and saves its Stack Frame in RAM. The function remain frozen untill it is called again.
2. Generator Expression consumes less memory than List Compresion .
3. Generator allow Infinite Data Stream as it process one iteam at a time.
4. Once a generator is exhausted, it cannot be reused. 
5. When a generator runs out of items it raises a StopIteration exception.
6. Generator can transform, filter, and process data modularly by chaining generators together.
7. The yield from syntax is used to delegate all of its operations to another generator or iterable.
8. .send() method allows  to pass values back into a generator, turning it into a coroutine. 