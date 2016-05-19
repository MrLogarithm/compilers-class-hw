import sys, os, optparse, shutil

if __name__ == '__main__':
    optparser = optparse.OptionParser()
    optparser.add_option("-a", "--answerdir", dest="answer_dir", default='answer', help="answer directory containing your source files")
    optparser.add_option("-z", "--zipfile", dest="zipfile", default='source', help="zip file you should upload to Coursys (courses.cs.sfu.ca)")
    (opts, _) = optparser.parse_args()

    outputs_zipfile = shutil.make_archive(opts.zipfile, 'zip', opts.answer_dir)
    print >>sys.stderr, "%s created" % (outputs_zipfile)

