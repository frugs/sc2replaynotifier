from sc2reader.resources import Replay

from sc2replaynotifier import ReplayHandler, create_replay_notifier


class DebugReplayHandler(ReplayHandler):

    async def handle_replay(self, replay: Replay):
        print([player.name for player in replay.players])


replay_notifier = create_replay_notifier(DebugReplayHandler())

replay_notifier.handle_replays()