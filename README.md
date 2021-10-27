
# Vocabulary-Scrapper

This little module, will create sample JSON API due to a collection ID on ***vocabulary.com*** providing different vocabularies for English language learners.

## Usage

1. First, you need to run Flask:

**Bash:**
```bash
$ export FLASK_APP=hello
$ flask run
 * Running on http://127.0.0.1:5000/
```
or **CMD**:
```bash
> set FLASK_APP=hello
> flask run
 * Running on http://127.0.0.1:5000
```
or **Powershell**:
```bash
> $env:FLASK_APP = "hello"
> flask run
 * Running on http://127.0.0.1:5000/
```

2. Then, open *localhost:5000* and you see a welcome text.

After that, enter the url below:
```bash
localhost:5000/api/[COLLECTION_ID]
```
For the `[COLLECTION_ID]`, enter the collection ID from **vocabulary.com**.

3. Finally, the sample API created based on the collection you've specified is ready!
