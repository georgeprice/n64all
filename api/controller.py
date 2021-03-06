from input_types import InputTypes
from input import Input, Analog


class Controller:

    def __init__(self):
        self._buttons = {
            InputTypes.ANALOG.value: Analog(),

            InputTypes.LEFT_TRIGGER.value: Input(),
            InputTypes.RIGHT_TRIGGER.value: Input(),

            InputTypes.A_BUTTON.value: Input(),
            InputTypes.B_BUTTON.value: Input(),
            InputTypes.Z_BUTTON.value: Input(),

            InputTypes.C_UP_ARROW.value: Input(),
            InputTypes.C_LEFT_ARROW.value: Input(),
            InputTypes.C_RIGHT_ARROW.value: Input(),
            InputTypes.C_DOWN_ARROW.value: Input(),

            InputTypes.D_UP_ARROW.value: Input(),
            InputTypes.D_LEFT_ARROW.value: Input(),
            InputTypes.D_RIGHT_ARROW.value: Input(),
            InputTypes.D_DOWN_ARROW.value: Input(),

            InputTypes.START.value: Input(),
        }

    def get_button(self, button):
        if button is None:
            raise ValueError("Button can't be none mate")

        if isinstance(button, InputTypes):
            if button.value not in self._buttons:
                raise ValueError("Not a button mate")
            return self._buttons.get(button.value, None)
        elif isinstance(button, str):
            if button not in self._buttons:
                raise ValueError("Not a button mate")
            return self._buttons.get(button, None)

    def get_state(self):
        return {i: s.get_state() for i, s in self._buttons.items()}

    def __str__(self):
        return "\n".join(["{} = {}".format(button, str(state)) for button, state in self._buttons.items()])

