from sc2replaynotifier import ReplayHandler, create_replay_notifier


class DebugReplayHandler(ReplayHandler):

    async def handle_replay(self, replay: str):
        print(str)


replay_notifier = create_replay_notifier(DebugReplayHandler())

replay_notifier.handle_replays()