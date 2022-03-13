from game.scripting.action import Action


# TODO: Implement MoveActorsAction class here!
# Action class will be overriden
class MoveActorsAction(Action):

    # Override the execute(cast, script) method as follows:
    def execute(self, cast, script):
        """Executes something that is important in the game. This method should be overriden by 
        derived classes.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # 1) get all the actors method from the cast
        actors = cast.get_all_actors()
        # 2) loop through the actors
        for actor in actors:
            # 3) call the move_next() method on each actor
            actor.move_next()
