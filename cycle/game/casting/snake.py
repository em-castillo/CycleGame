import constants
import random
from game.casting.actor import Actor
from game.shared.point import Point


class SnakeModel(Actor):
    """
    A long limbless reptile.

    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """

    def __init__(self):
        super().__init__()
        self._segments = []
        self._prepare_body()
        self._points = 0

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        pass

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)

    def _prepare_body(self):
        pass

    def reset(self):
        """Selects random points"""
        self._points = random.randint(1, 8)

    def get_points(self):
        """Gets the points.

        Returns:
            points (int): The points.
        """
        return self._points


class Snake(SnakeModel):
    """
    First long limbless reptile.

    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """

    def __init__(self):
        super().__init__()

    def get_segments(self):
        return super().get_segments()

    def move_next(self):
        return super().move_next()

    def get_head(self):
        return super().get_head()

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(constants.GREEN)
            self._segments.append(segment)

    def turn_head(self, velocity):
        return super().turn_head(velocity)

    def _prepare_body(self):

        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, 200)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = constants.YELLOW if i == 0 else constants.GREEN

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)

    def reset(self):
        return super().reset()

    def get_points(self):
        return super().get_points()


class Snake2(SnakeModel):
    """
    Second long limbless reptile.

    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """

    def __init__(self):
        return super().__init__()

    def get_segments(self):
        return super().get_segments()

    def move_next(self):
        return super().move_next()

    def get_head(self):
        return super().get_head()

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(constants.BLUE)
            self._segments.append(segment)

    def turn_head(self, velocity):
        return super().turn_head(velocity)

    def _prepare_body(self):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, 400)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = constants.RED if i == 0 else constants.BLUE

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)

    def reset(self):
        return super().reset()

    def get_points(self):
        return super().get_points()
