"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start = 0):
        """Make a new generator, defin start and current values"""
        self.start = start
        self.current = start 

    def __repr__(self):
        """Show representation."""

        return f"<SerialGenerator start={self.start} next={self.current + 1}>"

    def describe(self):
        """Descripte the class."""
        return f"I am a serial number currenly set to {self.start}, and the next number will be {self.current + 1}."

    def generate(self):
        """Generate new numer and save to variable 'current'."""
        serial = self.current
        self.current += 1
        return serial
    
    def reset(self): 
        """Reset the current value back to the start."""
        self.current = self.start 