# MelbDjango School Lesson Three

**Important:** Please take the [survey](https://docs.google.com/a/acommoncreative.com/forms/d/1VKqD1-aVsgztk19kdluNtFyTGiarbV9LgBFi2BwYT-g/viewform?c=0&w=1) if you came to the class today.

The slides for this lesson are [available online](https://melbdjango.github.io/lesson-three/).

Congratulations, you've made it to the git repository for our third lesson. Hopefully you also made it to the class
and some of this makes sense to you.

Check our RESOURCES.md for some links we think you'll find handy.


## Homework Checklist

- [ ] Read up on regular expressions
- [ ] [Fork this repository][gh-fork]
- [ ] Clone the repo to your own machine
- [ ] Use the virtualenv you created in previous lesson
- [ ] Add urls for clients and projects
- [ ] Update the templates to use `{% url %}`
- [ ] Create views that list `Clients` and `Projects`
- [ ] Use template inheritance to avoid having the same code in all of your templates
- [ ] Bonus points: Create a client summary page that lists all of it's projects and time entries

When you've completed some or all of the homework please make a [Pull Request][gh-pr] against this repository. If you submit
your work before Wednesday evening we'll give you feedback before the next class.

If you'd like help, make a Pull Request with your incomplete work and ask a question to @darrenfrenkel, @sesh or
@funkybob.

## Displaying the class slides

Install reveal-md with npm and use that to display the class slides.

```
    npm install -g reveal-md
```

From within the `lesson-three` repo:

```
    cd slides
    reveal-md CLASS.md --theme melbdjango
```

[gh-fork]: https://help.github.com/articles/fork-a-repo/
[gh-pr]: https://help.github.com/articles/using-pull-requests/
[dj-request-response]: https://docs.djangoproject.com/en/1.8/ref/request-response/
[mdn-html]: https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Introduction
