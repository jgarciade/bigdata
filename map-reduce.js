// User per programming language
var m = function () {
    var data = this["programming_languages"];
    if (data != NaN && data != null) {
        data.forEach(element => {
            if (!element.includes(" ", ",")) {
                emit(element, 1);
            }
        });
    }
}

var r = function (key, values) {
    return Array.sum(values)
}

db.data.mapReduce(m, r, { out: 'map_res' })

