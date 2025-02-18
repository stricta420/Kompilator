class CustomError(Exception):
    pass

class CodeError(CustomError):
    def __init__(self, line, error_message):
        super().__init__(f"Error at line {line}, with error message: {error_message}")
        self.line = line
        self.error_message = error_message

class InterpreterError(CodeError):
    def __init__(self, line, error_message):
        super().__init__(line, f"Error during Interpretation (logic): {error_message}")


class LexerError(CodeError):
    def __init__(self, line, error_message):
        super().__init__(line, f"Error during syntax characters check: {error_message}")


class PerserError(CodeError):
    def __init__(self, line, error_message):
        super().__init__(line, f"Error during syntax logic check (Perser): {error_message}")

class VariableNotFoundError(InterpreterError):
    def __init__(self, line, error_message, var_name):
        super().__init__(line, f"Variable {var_name} dosnt exist!. More info: {error_message}")

class VariableOfWrongType(InterpreterError):
    def __init__(self, line, error_message, var_name):
        super().__init__(line, f"Variable {var_name} has wrong type for this operation!. More info: {error_message}")


class IteratorError(CodeError):
    def __init__(self, line, error_message):
        super().__init__(line, f"Error in for loop - cant change value of iterator: {error_message}")

class ProcedureCreatedTwice(CodeError):
    def __init__(self, line, error_message, procedure_name):
        super().__init__(line, f"Procedure: {procedure_name} create twice at line {line} additional message: {error_message}")

class ProcedureDosntExist(CodeError):
    def __init__(self, line, error_message, procedure_name):
        super().__init__(line, f"Procedure: {procedure_name} called at line {line} dosnt exist, additional message: {error_message}")

class ProcedureCalledWithWrongAmoutOfArguments(CodeError):
    def __init__(self, line, error_message, procedure_name):
        super().__init__(line, f"Procedure: {procedure_name} called at line {line} takes diffrent amount of arguments, additional message: {error_message}")
