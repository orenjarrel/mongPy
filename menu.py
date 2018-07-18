from database import Database
from models.blog import Blog


class Menu(object):
    def __init__(self):
        # Ask user for author name
        # Check if they've already have an account
        # If not prompt them to create one

        self.user = input("Enter your author name: ")
        self.user_blog = None
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        # check to see if there is a blog with this author name
        # below: find one blog that has the author as the user (which was entered)
        blog = Database.find_one('blogs', {'author': self.user}) is not None
        if blog is not None:
            self.user_blog = blog
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Enter blog title: ")
        description = input("Enter blog description: ")
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        # User  read or write blogs?
        read_or_write = input("Do you want to read (R) or write (W) blogs? ")

        if read_or_write == 'R':
            # list blogs in database
            # allow user to pick one
            # display posts
            pass
        elif read_or_write == 'W':
            # prompt to create new blog
            pass
        else:
            print("Thank you for blogging!")