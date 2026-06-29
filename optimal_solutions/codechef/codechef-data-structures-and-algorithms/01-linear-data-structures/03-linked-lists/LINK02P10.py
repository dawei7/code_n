


def solve():
    class Node:
        def __init__(self, songId):
            self.songId = songId
            self.prev = None
            self.next = None

    class MusicPlayer:
        def __init__(self):
            self.head = None
            self.currentSong = None

        # Function to add a song to the end of the list
        def addSong(self, songId):
            newNode = Node(songId)

            if self.head is None:
                self.head = newNode
                self.currentSong = newNode
                return

            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode
            newNode.prev = temp

        # Function to play the next song
        def playNext(self):
            if self.currentSong.next is not None:
                self.currentSong = self.currentSong.next

        # Function to play the previous song
        def playPrev(self):
            if self.currentSong.prev is not None:
                self.currentSong = self.currentSong.prev

        # Function to switch to a specific song
        def switchSong(self, songId):
            temp = self.head
            while temp is not None:
                if temp.songId == songId:
                    self.currentSong = temp
                    return
                temp = temp.next

        # Function to return the songId of the current song playing
        def current(self):
            return self.currentSong.songId

    # Main function to test the music player
    if __name__ == "__main__":
        player = MusicPlayer()
        queries = int(input())
        while queries > 0:
            line = input().split()
            query = int(line[0])

            if query == 1:
                songId = int(line[1])
                player.addSong(songId)
            elif query == 2:
                player.playNext()
            elif query == 3:
                player.playPrev()
            elif query == 4:
                songId = int(line[1])
                player.switchSong(songId)
            elif query == 5:
                print(player.current())
            else:
                print("Invalid query!")
            queries -= 1


if __name__ == "__main__":
    solve()
