import sys
import subprocess
import csv
from optparse import OptionParser

import settings

def load_people(filename="people.csv"):
    r = csv.reader(open(filename))
    people = {}
    for person in r:
        people[person[0]] = [person[1], person[2]]
        if not person[1]:
            people[person[0]][0] = person[0].title()
    return people

def save_person(nick, desc, name=None, filename="people.csv"):
    with open(filename, 'ab') as csvfile:
        w = csv.writer(csvfile)
        w.writerow([nick, name, desc])

def write_introduction(people, message):
    i = " & ".join([v[0] for n,v in people.items()]) + ", please meet.\n\n"
    i += "\n\n".join([v[1] for n,v in people.items()])
    if message:
        i += "\n\n" + message
    else:
        i += "\n\n" + settings.closing
    i += "\n\n" + settings.valediction + ",\n\n" + settings.name
    return i


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-a", "--add", dest="add", action="store_true")
    parser.add_option("-m", "--message", dest="message", default=False, action="store")
    (options, args) = parser.parse_args()

    if options.add: # we're adding a new person
        if len(args) == 2:
            save_person(args[0], args[1])
        else:
            save_person(args[0], args[2], args[1])

    else: # write the intro
        people = load_people()

        introducing = {} # get the people data from the set
        for person in args:
            try:
                introducing[person] = people[person]
            except KeyError, e:
                print "Missing person %s in your data!" % e
                sys.exit()

        msg = write_introduction(introducing, options.message)
        print msg
        p = subprocess.Popen(["pbcopy"],stdin=subprocess.PIPE)
        p.stdin.write(msg)
